window.resize_book_shelves = function () {
    return $(".book-shelf").each(function (e, t) {
        var books, n, s, o, a, r, l, u, c;
        books = $(t).find(".book-shelf-book");
        n = books.filter("[data-featured]");
        o = books.not("[data-featured]");
        books.height("");
        $(document).width() > 767 && (u = [], o.each(function (e, t) {
            return u.push($(t).height()) ;
        }),
        l = Math.max.apply(null, u), o.height(l),
         n.height(2 * l + 2 * parseInt(o.css("padding-bottom")) + parseInt(o.css("margin-bottom"))), 
         (s = n.find("hr")).length > 0) ? (
         	r = s.position().top, c = n.height() - r - 30, n.find(".full").css("max-height", c), 
         	n.find(".description").removeClass("is-hidden"),
         	a = $('<a class="see_more">ادامه</a>').attr("href", n.find(".title a").attr("href")),
         	n.find(".description .full").dotdotdot({after: a, watch: window})
         ) : void 0 ;
    });
};
function search(){
	var term = $("#search-query").val();
	location.replace("/search/"+term);
};
window.navid_resize_book_shelves = function () {
    return $(".book-shelf").each(function (e, t) {
        var books, n, s, o, a, r, l, u, c;
        books = $(t).find(".navid-book-shelf-book");
        n = books.filter("[data-featured]");
        o = books.not("[data-featured]");
        books.height("");
        $(document).width() > 767 && (u = [], o.each(function (e, t) {
            return u.push($(t).height()) ;
        }),
        l = Math.max.apply(null, u), o.height(l),
         n.height(l), 
         (s = n.find("hr")).length > 0) ? (
         	r = s.position().top, c = n.height() - r - 30, n.find(".full").css("max-height", c), 
         	n.find(".description").removeClass("is-hidden"),
         	n.each(function(e2,t2){
         		a = $('<a class="see_more">ادامه</a>').attr("href", $(t2).find(".title").attr("href"));
         		$(t2).find(".description .full").dotdotdot({after: a, watch: window});
         	})
         	
         ) : void 0 ;
    });
};

