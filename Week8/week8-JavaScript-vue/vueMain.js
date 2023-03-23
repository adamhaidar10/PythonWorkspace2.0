// create a Vue app
const app = Vue.createApp(
    {
        data()
        {
            return {pagename: "Views",
                    description: "This is a page about the beautiful views of the world",
                    mainimage: "northernLights.jpg",
                    wikilink: "https://en.wikipedia.org/wiki/Aurora",
                    stars: true,
                    view: "tree",
                    famousviews: ["Pyramids", "Great Wall of China", "Easter Island"],
                    // famous: [{country: "Egypt", continent: "Africa", image: "pyramids.jpg", name: "Pyramids of Giza"},
                    //          {country: "China", continent: "Asia", image: "greatwall.jpg", name: "Great Wall of China"},
                    //          {country: "Chile", continent:"South America", image:"easterisland.jpg", name: "Easter Island"}],
                    likes: 0,
                    happy: false
                }
                    
                            

        },
        methods:
        {
            likesviews()
            {
                this.likes++;
                this.happy = true;
            },
            dislikesviews()
            {
                this.likes--;
                if (this.likes < 0)
                {
                    this.likes = 0
                }
                if (this.likes == 0)
                {
                    this.happy = false;
                }

            },
            send_details()
            {
                console.log("hello from send_details")
            }
            // viewhover(viewimg)
            // {
            //     console.log("hello")
            //     document.getElementById("viewimg").src = viewimg;
            // }
        }
        
        


    })
