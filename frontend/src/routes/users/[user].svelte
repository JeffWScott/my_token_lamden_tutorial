<!-- frontend/src/routes/users/[user].svelte -->
<script context="module">
   export async function preload({ params, query }) {
      const res = await this.fetch(`http://localhost:3737/contracts/my_token/S?key=${params.user}`)
      const data = await res.json();
      if (typeof data.value === 'undefined') this.error(res.status, data.message);
      if (data.value === null) data.value = 0;
      return { value: data.value, user: params.user };
   }
</script>

<script>
   import { goto } from '@sapper/app';

   export let user;
   export let value;

   let receiver = "";
   let amount = 0;

   const transfer = async () => {
      const transaction = {
         sender: user,
         contract: 'my_token',
         method: 'transfer',
         args: {
            receiver,
            amount
         }
      }

      const options = {
         method: 'POST',
         headers: {
            'Content-Type': 'application/json'
         },
         body: JSON.stringify(transaction)
      }

      const res = await fetch(`http://localhost:3737/`, options)
      const data = await res.json();
      if (data.error) {
         alert(data.error);
      }else{
         alert("You sent " + amount + " token(s) to " + receiver + "!");
         refreshBalance();
         clearInputs();
      }
   }

   const refreshBalance = async () => {
      const res = await fetch("http://localhost:3737/contracts/my_token/S?key=" + user)
      let data = await res.json();
      value = data.value;
   }

   const clearInputs = () => {
      receiver = ""
      amount = 0
   }

   const logout = () => {
      goto(`.`);
   }
</script>

<style>
   p{
      font-size: 1.2em;
   }
   .shadowbox{
      padding: 0.5rem 20px;
   }
   form{
      padding: 50px;
      color: #461BC2;
      display:flex;
      flex-direction: column;
      border: none;
      box-sizing: border-box;
   }
   form > h2{
      margin: 0;
      font-weight: 600;
      line-height: 2.2;
      letter-spacing: 1px;
   }
   form > input{
      margin-bottom: 1rem;
   }
   input[type="submit"] {
      margin-right: 20px;
   }
   .buttons {
      display: flex;
      flex-direction: row;
      justify-content: flex-end;
      margin-top: 1rem;
   }
</style>

<svelte:head>
   <title>{user + "'s Tokens"}</title>
</svelte:head>

<h1>{"Hello " + user + "!"}</h1>
<div class="shadowbox">
   <p><strong>Token Balance:</strong> {value}</p>
</div>

<form on:submit|preventDefault={transfer}>
   <h2>Enter Transfer Details</h2>
   <label for="to">To</label>
   <input type="text" name="to" bind:value={receiver} required="true"/>
   <label for="amount">Token Amount</label>
   <input type="number" name="amount" bind:value={amount} required="true"/>
   <div class="buttons">
      <input class="button" type="submit" value="send"/>
      <button class="button" on:click={logout}>sign out </button>
   </div>
</form>

