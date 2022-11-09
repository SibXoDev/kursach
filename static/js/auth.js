"use strict";
SXDAPI.contextMenu.defaultContextMenu = true;

window.addEventListener("load", () => {
    // const csrftoken = document.body.querySelector("input[name='csrfmiddlewaretoken']").value;
    let hideForm = document.body.querySelector("form.hide");
    const urlParams = new URLSearchParams(window.location.search);

    SXDAPI.connect("/auth?check=true", "",
        {
            method: "GET",
            mode: "same-origin",
            credentials: "same-origin",
            cache: "default",
            headers: {
                "Accept": "application/json"
            }
        },
        (result) => {
            if (result.auth) window.location.href = urlParams.get("next") || "/";
        },
        (error) => {},
        true
    );

    document.body.querySelectorAll("form").forEach(form => {
        form.querySelectorAll("button").forEach(bt => {
            // let password = form.querySelector("input[name='password']");
            // let username = form.querySelector("input[name='username']");

            bt.disabled = false;
            if (bt.type == "button") {
                bt.onclick = (e) => {
                    form.classList.add("hide");
                    hideForm.classList.remove("hide");
                    hideForm = form;
                    e.preventDefault();
                    return false;
                };
            } else if (bt.type == "submit") {
                bt.onclick = (e) => {
                    if (hideForm != form) {

                        const btText = bt.textContent;
                        bt.textContent = "Обработка...";
                        bt.disabled = true;

                        SXDAPI.connect(`${form.id == "login" ? "/auth/" : "/register/"}`, "", {
                            method: "POST",
                            mode: "same-origin",
                            credentials: "same-origin",
                            cache: "default",
                            headers: {
                                // "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                // "Content-Type": "application/json",
                                "Accept": "application/json"
                            },
                            body: new FormData(form)
                        },
                        (result) => {
                            if (result.auth) {
                                bt.textContent = "Успешно";
                                window.location.href = urlParams.get("next") || "/";
                            } else if (result.message) {
                                let time = 3000;
                                let messages = result.message;

                                if (typeof result.message === "object") {
                                    messages = [];
                                    Object.keys(result.message).forEach(key => {
                                        const messageList = result.message[key];
                                        messageList.forEach(message => {
                                            if (key.indexOf("password") != -1) {
                                                message = message.replace("это значение", "пароль");
                                            };
                                            messages.push(message);
                                        });
                                    });
                                    messages = messages.join("<br><br>");
                                    time = 6000;
                                };

                                SXDAPI.description.show({
                                    textHTML: messages,
                                    color: "rgb(220, 0, 0)",
                                    time: time
                                });
                            };

                            bt.disabled = false;
                            bt.textContent = btText;
                        },
                        (error) => {
                            bt.disabled = false;
                            bt.textContent = btText;
                        }, true);

                    };
                    e.preventDefault();
                    return false;
                };
            };
        });
    });
});