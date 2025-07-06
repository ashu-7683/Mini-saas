<script lang="ts">
    import { user } from "$lib/stores/auth";
    import { goto } from "$app/navigation";

    let email = "";
    let password = "";
    let error = "";

    async function handleLogin() {
        const res = await fetch("/api/auth/token", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ username: email, password, grant_type: "password" }),
        });

        if (res.ok) {
            const { access_token } = await res.json();
            localStorage.setItem("token", access_token);
            user.set({ email, token : access_token });
            goto("/");
        } else {
            error = "Invalid credentials";
        }
    }
    </script>

    <div class="max-w-md mx-auto mt-10">
    <h1 class="text-2xl font-bold mb-6">Login</h1>
    {#if error}
        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
        {error}
        </div>
    {/if}
    <form on:submit|preventDefault={handleLogin}>
        <input
        type="email"
        bind:value={email}
        placeholder="Email"
        class="w-full p-2 mb-4 border rounded"
        required
        />
        <input
        type="password"
        bind:value={password}
        placeholder="Password"
        class="w-full p-2 mb-4 border rounded"
        required
        />
        <button
        type="submit"
        class="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
        >
        Login
        </button>
    </form>
</div>