class Renderer {
    recipeRender(recipes:Recipe[]){
        const recipesEle = $(".recipes-container")
        var scource = $("#recipes-template").html();
        var template = Handlebars.compile(scource);
        var newHTML = template({ recipes : recipes} );
        recipesEle.empty().append(newHTML)
    }
}
