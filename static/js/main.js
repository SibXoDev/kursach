SXDAPI.contextMenu.defaultContextMenu = true;

function getCookie(name) {
    const matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
    return matches ? decodeURIComponent(matches[1]) : undefined;
};

function setCookie(name, value, options = {}) {
    options = {
        path: "/",
        secure: true,
        ...options
    };

    if (options.expires instanceof Date) options.expires = options.expires.toUTCString();

    let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

    for (let optionKey in options) {
        updatedCookie += "; " + optionKey;
        const optionValue = options[optionKey];
        if (optionValue !== true) updatedCookie += "=" + optionValue;
    };

    document.cookie = updatedCookie;
};

function checkTheme() {
    if (!document.body) return;
    if (theme) {
        document.body.classList.remove("white-theme");
        setCookie("theme", "black", {"max-age": 604800});
    } else {
        document.body.classList.add("white-theme");
        setCookie("theme", "white", {"max-age": 604800});
    };
};

const csrftoken = getCookie("csrftoken");

if (getCookie("theme") === undefined) setCookie("theme", "black", {"max-age": 604800});
let theme = getCookie("theme") === "black";

window.addEventListener("DOMContentLoaded", () => {
    document.body.classList.add("load");
    checkTheme();
    setTimeout(() => document.body.classList.remove("load"), 20);

    const btChangeTheme = document.querySelector("#change-theme");

    if (!btChangeTheme) return;

    btChangeTheme.onclick = () => {
        theme = !theme;
        checkTheme();
    };
});