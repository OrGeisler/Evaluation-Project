let dataModule = new DataModule()
let renderer: Renderer = new Renderer()

$('.search').on('click',async function () {
    const ingredientName:any= $('#ingredient').val()
    const fillterGluten : boolean = $('.gluten').is(":checked")
    const fillterDairy : boolean = $('.dairy').is(":checked")
    await dataModule.recipeGeneratoer(ingredientName,fillterGluten,fillterDairy)
    renderer.recipeRender(dataModule.ingredientList)
    console.log(dataModule.ingredientList)
})

$('.recipes-container').on('mouseenter' ,'.img-fluid',function(){
    const ingredients = $(this).closest('.card').data().id
    $(this).popover({title: "<h3><strong>First Ingredient</strong><h3>", 
    content: `${dataModule.splitIngredients(ingredients)}`,html:true})}    );