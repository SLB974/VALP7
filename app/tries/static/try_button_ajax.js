$(document).ready(function() {
    $("form").submit(function(event) {
        if ($("#username").val().length === 0) {
            alert("Veuillez remplir le champ");
            event.preventDefault();
        } else {
            let chaine = $("form").serialize();
            console.log(chaine);
        }
    });
});