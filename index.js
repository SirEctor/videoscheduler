const { Client } = require("youtubei");
const youtube = new Client();


const run = async (channelUsername, series) => {
    const channels = await youtube.search(channelUsername, {
        type: "channel"
    });

    console.log(channels.items);
};

// $.ajax({
//     type: "POST",
//     url: "/videoscheduler/scrape.py",
//     data: { param: text}
//   }).done(function( o ) {
//      // do something
//      console.log("python finished, back in index.js");
// });

function handleYaas(){
    let channelUsername = document.getElementById('channel-input').value;
    let series = document.getElementById('series-input').value;

    console.log(channelUsername);
    console.log(series);
    run(channelUsername, series);
}