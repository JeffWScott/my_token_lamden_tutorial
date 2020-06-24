<!-- frontend/src/routes/index.svelte -->
<script>
   import { goto } from '@sapper/app';

   let user = ""

    const login = () => {
      goto('/users/' + user);
   }
</script>

<style>
   *{
      text-align: center;
   }
</style>

<svelte:head>
   <title>My Token</title>
</svelte:head>

<h1>Welcome to My Token</h1>

<form on:submit|preventDefault={login}>
   <p>Check your token balance</p>
   <input type="text" bind:value={user} required="true"/>
   <input class="button" type="submit" value="sign in" />
</form>