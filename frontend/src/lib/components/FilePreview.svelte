<script lang="ts">
    export let fileUrl: string;

    function isPdf(url: string) {
        return url?.endsWith('.pdf');
    }
    </script>

    {#if fileUrl}
    {#if isPdf(fileUrl)}
        <iframe src={fileUrl} width="100%" height="500px" />
    {:else}
        <img src={fileUrl} alt="Preview" class="max-w-full" />
    {/if}
{/if}