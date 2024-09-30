<script>
    function switchTheme(theme) {
    const themeLink = document.getElementById('theme-link');
    const body = document.body;

    if (theme === 'dark') {
    themeLink.href = "{% static 'css/dark-theme.css' %}";
    body.style.backgroundColor = '#343a40';  // Define o fundo cinza para o tema escuro
} else {
    themeLink.href = "{% static 'css/light-theme.css' %}";
    body.style.backgroundColor = '';  // Reseta o fundo para o tema claro
}
    document.cookie = `theme=${theme};path=/`;
}

    document.addEventListener('DOMContentLoaded', (event) => {
    const theme = "{{ theme }}";
    switchTheme(theme);
});
</script>