var input = document.querySelectorAll("input");

var newarr = Array.from(input);

// for adding blue border in input field while in focus
newarr.forEach((item)=>{
    item.addEventListener('focus', (event)=>{
        event.target.style.boxShadow = "3px 3px 5px 2px rgba(0, 0, 255, 0.8)";
        console.log(event.target.style);
    })

    item.addEventListener('blur', (event)=>{
        event.target.style.boxShadow = "";
        console.log(event.target.style);
    })
})

// for closing the flash messages after submitting the form
document.querySelectorAll("div.message-box").forEach((box)=>{
    let btn = box.lastElementChild;
    btn.addEventListener('click', ()=>{
        box.style.display = "none";
    })
})