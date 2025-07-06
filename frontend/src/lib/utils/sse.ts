export function subscribeToIssues(callback: (issues: any[]) => void) {
    const eventSource = new EventSource('/api/issues/events')
    
    eventSource.addEventListener('issues_update', (e) => {
        callback(JSON.parse(e.data))
    })
    
    return () => eventSource.close()
    }