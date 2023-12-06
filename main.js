var slideimages = ["slide1.jpg", "slide2.gif", "slide3.gif", "slide4.jpg", "slide5.gif"];
var currentSlide = 0;

function showSlide(){
    document.getElementById('slide').src = "assets/"+slideimages[currentSlide];
}


function nextSlide(){
    currentSlide = (currentSlide + 1) % slideimages.length;
    showSlide()
}

function prevSlide(){
    currentSlide = (currentSlide - 1 + slideimages.length) % slideimages.length;
    showSlide()
}


function showSlideN(slideNumber){
    currentSlide = slideNumber - 1;
    showSlide();
}
