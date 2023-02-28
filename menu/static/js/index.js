const toggls = document.querySelectorAll('.caret');


toggls.forEach( elem=>{
    elem.addEventListener('click',()=>{
        elem.parentElement.querySelector(".nested").classList.toggle("active");
        elem.classList.toggle("caret-down");
    })
})

