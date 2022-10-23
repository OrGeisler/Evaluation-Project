class Recipe {
    ingredients:string[];
    title: string;
    thumbnail: string;
    href: string;

    constructor(
        ingredients:string[],
        title: string,
        thumbnail: string,
        href: string
      )

      {
        this.ingredients=ingredients,
        this.title = title;
        this.thumbnail = thumbnail;
        this.href = href;
      }
    }

