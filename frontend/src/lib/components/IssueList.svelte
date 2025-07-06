<script lang="ts">
    import { onMount } from 'svelte'
    import IssueCard from './IssueCard.svelte'
    
    export let issues: any[] = []
    
    onMount(async () => {
        const res = await fetch('/api/issues', {
        headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
        })
        issues = await res.json()
    })
    </script>

    <div class="space-y-4">
    {#each issues as issue}
        <IssueCard {issue} />
    {/each}
</div>