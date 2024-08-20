/*=============== SEARCH ===============*/
const searchButton = document.getElementById('search-button'),
        sreachClose = document.getElementById('search-close'),
        searchContent = document.getElementById('search-content')


/*=============== MENU SHOW ===============*/
// valodate of constant exists 
if(searchButton){
    searchButton.addEventListener('click' , ()=> {
        searchContent.classList.add('show-search')
    })
}

/*=============== MENU hidden ===============*/
// valodate of constant exists 
if(sreachClose){
    sreachClose.addEventListener('click' , () =>{
        searchContent.classList.remove('show-search')
    })
}


/*=============== LOGIN ===============*/


/*=============== ADD SHADOW HEADER ===============*/
const shadowHeader = () => {
    const header = document.getElementById('header')

    this.scrollY >= 50 ? header.classList.add('shadow-header')
                       : header.classList.remove('shadow-header')
}
window.addEventListener('scroll',shadowHeader)

/*=============== HOME SWIPER ===============*/
let swiperHome = new Swiper('.home__swiper', {
    loop: true,
    spaceBetween: -24,
    grabCursor: true,
    slidesPerView: 'auto',
    centeredSlides: 'auto',


    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },

    breakpoints: {
        1220: {
            spaceBetween: -32,
        }
    }
  });


/*=============== FEATURED SWIPER ===============*/


/*=============== NEW SWIPER ===============*/


/*=============== TESTIMONIAL SWIPER ===============*/


/*=============== SHOW SCROLL UP ===============*/ 


/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/


/*=============== DARK LIGHT THEME ===============*/ 


/*=============== SCROLL REVEAL ANIMATION ===============*/
