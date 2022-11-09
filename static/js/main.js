// SXDAPI.contextMenu.browserContextMenu = false;
// SXDAPI.contextMenu.autoShow = false;
SXDAPI.contextMenu.defaultContextMenu = true;

// SXDAPI.onload = () => {
//     if (!SXDAPI.isMobile) {
//         for (const card of document.getElementsByClassName("card")) {
//             let cardShadow = card.querySelector("img").cloneNode(true);
//             cardShadow.classList.add("card--shadow");

//             const position = SXDAPI.getOffset(card);

//             cardShadow.style.left = `${position.x}px`;
//             cardShadow.style.top = `${position.y}px`;
//             cardShadow.style.width = `${card.offsetWidth}px`;
//             cardShadow.style.height = `${card.offsetHeight}px`;

//             document.body.prepend(cardShadow);

//             card.onmouseover = function(e) {
//                 // cardShadow.classList.add("none-transition");
//                 this.classList.add("none-transition");
//             };

//             card.onmousemove = function(e) {
//                 const position = SXDAPI.getOffset(this);
//                 const coorX = e.offsetX;
//                 const coorY = e.offsetY;
//                 const w = this.offsetWidth;
//                 const h = this.offsetHeight;

//                 const posX = ~((w/2 - coorX) * (80/w)) / 5;
//                 const posY = ~~((h/2 - coorY) * (80/h)) / 5;

//                 cardShadow.style.left = `${position.x}px`;
//                 cardShadow.style.top = `${position.y}px`;
                
//                 cardShadow.style.width = `${w}px`;
//                 cardShadow.style.height = `${h}px`;

//                 this.style.transform = `rotateX(${posY}deg) rotateY(${posX}deg)`;
//                 cardShadow.style.transform = `translate(${(-2 * posX)}px, ${(2 * posY)}px)`;
//             };

//             card.onmouseleave = function(e) {
//                 this.style.transform = `rotateX(0) rotateY(0)`;
//                 cardShadow.style.transform = `translate(0px, 0px)`;
//                 cardShadow.classList.remove("none-transition");
//                 this.classList.remove("none-transition");
//             };
//         };
//     };
// };

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie("csrftoken");