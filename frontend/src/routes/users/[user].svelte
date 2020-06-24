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
   export let user;
   export let value;
</script>

<style>
   p{
      font-size: 1.2em;
   }
   .shadowbox{
      padding: 0.5rem 20px;
   }
</style>

<svelte:head>
   <title>{user + "'s Tokens"}</title>
</svelte:head>

<h1>{"Hello " + user + "!"}</h1>
<div class="shadowbox">
   <p><strong>Token Balance:</strong> {value}</p>
</div>
