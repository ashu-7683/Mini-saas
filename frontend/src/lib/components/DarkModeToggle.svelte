<script lang="ts">
    import { darkMode, toggleDarkMode } from '$lib/stores/theme';
    </script>

    <button on:click={toggleDarkMode} class="p-2 rounded-full">
    {#if $darkMode}
        <span>☀️ Light</span>
    {:else}
        <span>🌙 Dark</span>
    {/if}
</button>