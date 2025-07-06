import { writable } from 'svelte/store';

export const darkMode = writable(false);

export function toggleDarkMode() {
    darkMode.update(mode => {
        document.documentElement.classList.toggle('dark', !mode);
        return !mode;
    });
}