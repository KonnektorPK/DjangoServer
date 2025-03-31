export const showDialog = (text, title, button1, button2) => {
    document.getElementById("dialog_title").textContent = title;
    document.getElementById("dialog_text").textContent = text;

    const btnPrimary = document.getElementById("button_primary");
    const btnSecondary = document.getElementById("button_secondary");
    const footer = document.getElementById("dialog_footer");

    btnPrimary.textContent = button1;

    if (button2) {
        btnSecondary.textContent = button2;
        btnSecondary.classList.remove("hidden");
        footer.style.justifyContent = "";
    } else {
        btnSecondary.classList.add("hidden");
        footer.style.justifyContent = "center";
    }

    document.getElementById("overlay_alert").style.visibility = "visible";
    document.getElementById("overlay_alert").style.opacity = "1";
}

export const message = (text, title) => {
    if (title) {
        document.getElementById("dialog_title").textContent = title;
    } else {
        document.getElementById("dialog_title").textContent = 'Ошибка';
    }
    document.getElementById("dialog_text").textContent = text;

    document.getElementById("overlay_alert").style.visibility = "visible";
    document.getElementById("overlay_alert").style.opacity = "1";
}

export const hideDialog = () => {
    document.getElementById("overlay_alert").style.opacity = "0";
    document.getElementById("overlay_alert").style.visibility = "hidden";
}

document.getElementById("button_primary").addEventListener("click", hideDialog);
document.getElementById("button_secondary").addEventListener("click", hideDialog);