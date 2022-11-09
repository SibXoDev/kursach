window.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.querySelector("#search");
    const searchButton = document.querySelector("#search-bt");

    if (searchInput) {
        const getParam = new URLSearchParams(window.location.search);
        searchInput.value = getParam.get("search") || "";
        searchInput.onkeyup = (e) => {
            if (e.key === "Enter") {
                searchInput.value = searchInput.value.trim();
                window.location.search = `search=${searchInput.value}&category=${getParam.get("category") || ""}`;
            };
        };
        if (searchButton) {
            searchButton.onclick = () => {
                searchInput.value = searchInput.value.trim();
                window.location.search = `search=${searchInput.value}&category=${getParam.get("category") || ""}`;
            };
        };
    };
});