<!-- frontend/src/routes/_layout.svelte -->
<script>
   import Nav from '../components/Nav.svelte';
</script>

<style>
   main {
      position: relative;
      max-width: 56em;
      padding: 0 28px;
      margin: 0 auto;
      box-sizing: border-box;
   }
</style>

<Nav />
<main>
   <slot></slot>
</main>