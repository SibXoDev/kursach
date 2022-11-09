window.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.querySelector("#search");
    const searchButton = document.querySelector("#search-bt");

    if (searchInput) {
        searchInput.value = new URLSearchParams(window.location.search).get("search") || "";
        searchInput.onkeyup = (e) => {
            if (e.key === "Enter") {
                searchInput.value = searchInput.value.trim();
                window.location.search = `search=${searchInput.value}`;
            };
        };
        if (searchButton) {
            searchButton.onclick = () => {
                searchInput.value = searchInput.value.trim();
                window.location.search = `search=${searchInput.value}`;
            };
        };
    };
});