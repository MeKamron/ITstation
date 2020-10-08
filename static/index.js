// nav toggle active background
$('.navbar-toggler').click(function(){
    $('.navbar-toggler').toggleClass('active')

});

// nav link to pages
$('[data-scroll]').on('click', function(event){
    event.preventDefault();  

    var $this=$(this),
        blockId=$this.data('scroll'),
        blockOffset=$(blockId).offset().top;
   
   $('.nav-item').click(function(){
        $('.nav-item a').toggleClass('activeLink');
   });
        
   
   $('html, body').animate({
       scrollTop:blockOffset
   },1000);
});