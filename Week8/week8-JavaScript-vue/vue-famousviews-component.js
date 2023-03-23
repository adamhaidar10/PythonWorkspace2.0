app.component("famous-views",
{
    template:
    `<div>
    <p> Famous views</p>
    <div v-for="view in famous" v-on:mouseover="viewhover(view.image);" style="margin: 20px;">
        <p class="boreded_para">
            {{ view.country }} : {{ view.continent }} : {{ view.name }}
                </p>
                </div>
                <img id="viewimg" src="" style="width: 300px; height: 300px; border: 1px solid; background-color: pink;">

                </div>`,
    data()
    {
        famous: [{country: "Egypt", continent: "Africa", image: "pyramids.jpg", name: "Pyramids of Giza"},
                {country: "China", continent: "Asia", image: "greatwall.jpg", name: "Great Wall of China"},
                {country: "Chile", continent:"South America", image:"easterisland.jpg", name: "Easter Island"}]

    },

    methods:
    {
        console.log("hello")
        document.getElementById("viewimg").src = viewimg;

    }
}

)