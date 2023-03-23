app.component("details-form",
{
    template:
        `<form v-on:submit.prevent="on_submit">
        <p>
            Enter some details
        </p>
        <label for="field_name" style="margin: 10px;">Name</label>
        <input id="field_name" type="text" style="margin: 10px;" v-model="name">
        <br>
        <label for="field_details" style="margin: 10px;">Details</label>
        <input id="field_details" type="text" style="margin: 10px;" v-model="details">
        <br>
        <input type="submit" value="Submit form">
        </form>`,


    date()
    {
        return {
            name: "",
            details: ""
        }
    },

    methods:
    {
        on_submit()
        {
            console.log("submit");
            
            let entereddata = {name: this.name, details: this.details};
            this.$emit("data-entered", entereddata);

            this.name = "";
            this.details = "";




        }
    }
    
}


)