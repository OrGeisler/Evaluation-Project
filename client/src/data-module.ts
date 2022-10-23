class DataModule {
    ingredientList:Recipe[]
    
    constructor(){
        this.ingredientList = [] as Recipe[]
    }

    splitIngredients(ingredients:string) {
      var splitted = ingredients.split(",");
      return splitted[0];
      }
 
    async recipeGeneratoer(ingredient_name:string,fillterGluten:boolean,fillterDairy:boolean) {
        let response
        if ((!fillterGluten) && (!fillterDairy)) {
            response = await $.get(`/recipes/${ingredient_name}`)
        }
        else if ((fillterGluten) && (!fillterDairy)) {
          response = await $.get(`/recipes/${ingredient_name}?gluten_free=True`)
        }
        else if ((fillterDairy) && (!fillterGluten)) {
          response = await $.get(`/recipes/${ingredient_name}?dairy_free=True`)
        }  
        else {
          response = await $.get(`/recipes/${ingredient_name}?dairy_free=True&gluten_free=True`)
        }

        this.ingredientList = response.map((value:any) => {
            let recipe : Recipe = new Recipe(
                value.ingredients,
                value.title,
                value.thumbnail,
                value.href
            )
            return recipe
        })
    }
}

// module.exports = DataModule;
