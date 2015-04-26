/**
 * Created by himanshu on 4/25/15.
 */


console.log('hi');

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



function get_search_results(search_text){
    var csrftoken = getCookie('csrftoken');
    var jqxhr = $.post( "/search",
        {
            product_name: search_text,
            csrfmiddlewaretoken : csrftoken


        }
    );

    jqxhr.done(function(data) {

        rebuild_search_results_html(data);


      })
      .fail(function() {
        console.log( "error" );
      })
      .always(function() {
        console.log( "finished" );
    });
};

// {% for product in products %}
//
//        <div class="col-sm-4 col-lg-4 col-md-4">
//            <div class="thumbnail">
//
//                <img src="{{ product.picture }}" alt="pic">
//
//                <div class="caption">
//                    <h4 class="pull-right">${{ product.price }}</h4>
//                    <h4><a href='{% url 'price_check' %}?product_id={{ product.pk }}'>{{ product.title }}</a>
//                    </h4>
//                    <p>{{ product.description }}</p>
//                </div>
//                <div class="ratings">
//
//                    <p>
//                        {% for i in product.rating %}
//                            <span class="glyphicon glyphicon-star"></span>
//                        {% endfor %}
//
//                    </p>
//                </div>
//                <span class="pull-right">
//                    <strong>Coupons:</strong>
//                    {% for coupon in product.available_coupons %}
//                        {{  coupon.name }}
//                        {% empty %}
//                        Sorry, no coupons.
//                        {% endfor %}
//                </span>
//            </div>
//
//        </div>
//        {% empty %}
//        Sorry, you havent done anything yet.
//    {% endfor %}


//function result_to_html(result){
//  $('#search-results').add( "div").addClass("col-sm-4 col-lg-4 col-md-4");
//
//
//};


function rebuild_search_results_html(results){
    $('#search-results').empty();
    console.log(results);

    if(results.length===0){
        $('#search-results').append("<p>No Search Results.</p>");
    }
    else{
        $('#search-results').append("<h2>Search Results:</h2>");
    }



    for(var r =0; r<results.length; r++) {

        var code = ""
        code = "<a href=\"http://localhost:8000/price_check/?product_id="+results[r]['id']+"\">   "+results[r]['title']+"       </a> <br/>";

        console.log(code);
        $('#search-results').append(code);
    }
}


function search(){
    var product_name = $('#search_text').val();
    get_search_results(product_name);



    console.log(product_name);
};







$("#search_button").click(search);

