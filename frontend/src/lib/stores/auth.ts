import { writable } from 'svelte/store'

interface User {
    email: string
    role: string
    token: string
    }

    export const user = writable<User | null>(null)

    export async function login(email: string, password: string) {
    const res = await fetch('/api/auth/token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ username: email, password, grant_type: 'password' })
    })
    
    if (res.ok) {
        const { access_token } = await res.json()
        localStorage.setItem('token', access_token)
        
        // Fetch user details
        const userRes = await fetch('/api/users/me', {
        headers: { 'Authorization': `Bearer ${access_token}` }
        })
        const userData = await userRes.json()
        
        user.set({ ...userData, token: access_token })
        return true
    }
    return false
    }