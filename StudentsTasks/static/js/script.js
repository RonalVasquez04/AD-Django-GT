document.addEventListener('DOMContentLoaded', function () {
    var userDropdown = document.getElementById('userDropdown');
    var notasDropdown = userDropdown.querySelector('.dropdown-content');

    var menuVisible = false;

    userDropdown.addEventListener('click', function (event) {

        menuVisible = !menuVisible;
        notasDropdown.style.display = menuVisible ? 'block' : 'none';
    });

    document.addEventListener('click', function (event) {
        if (!userDropdown.contains(event.target)) {
            if (menuVisible) {
                menuVisible = false;
                notasDropdown.style.display = 'none';
            }
        }
    });
});
