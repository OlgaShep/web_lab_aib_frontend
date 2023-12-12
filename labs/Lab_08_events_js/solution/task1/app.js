document.addEventListener("DOMContentLoaded", () => {
let button = document.getElementsByClassName("buttons")
let body = document.querySelector("body")

console.log(body);

for (let i = 0 ; i < button.length ; i++) {
    button[i].addEventListener("click", function() {
        if (button[i].getAttribute("id") == "Crimson") {
            console.log(body);
            body.style['background-color'] = "Crimson";
        } else if (button[i].getAttribute("id") == "BlueViolet") {
            body.style['background-color'] = "BlueViolet";
        } else {
            body.style['background-color'] = "Navy";
        }
    })
}
})