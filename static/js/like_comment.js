
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

// operation for like

const like_operation = async (URL, total_like, postId) => {
    try {
        let response = await fetch(URL, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken,
            },
            body: JSON.stringify({
                "id": postId,
                "like": total_like
            }),
        });

        let data = await response.json();
        console.log(data); // Log the updated data from the backend
    } catch (error) {
        console.error('Error:', error);
    }
};

function add_like(button, postId) {
    let likecount = document.getElementById('count-like-' + postId);
    let currentlikes = parseInt(likecount.innerText);
    let id = parseInt(postId);
    let url = `https://blog-udis.onrender.com/post_api/${id}/`;

    // If the button already has 'Liked', it means the user is unliking the post
    if (button.classList.contains("btn-danger")) {
        button.classList.remove("btn-danger");
        button.classList.add("btn-outline-danger");
        button.innerText = "Like";
        currentlikes -= 1;  // Decrease the like count
    } else {
        button.classList.remove("btn-outline-danger");
        button.classList.add("btn-danger");
        button.innerText = "Liked";
        currentlikes += 1;  // Increase the like count
    }

    likecount.innerText = `${currentlikes} likes`; // Update the like count on the frontend

    // Now, send the updated like count to the backend
    like_operation(url, currentlikes, postId);
}




// Function to send comment data to the backend
const comment_operation = async (URL, comment) => {
    try {
        let response = await fetch(URL, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken,  // Ensure CSRF token is set
            },
            body: JSON.stringify({ "comments": comment }),
        });

        let data = await response.json();
        console.log("Server Response:", data); // Log the response from backend

        return data; // Return data in case you want to use it
    } catch (error) {
        console.error("Error:", error);
    }
};

// Function to handle comment submission
function submitComment(event, postId, username) {
    event.preventDefault(); // Prevent page reload

    let form = document.querySelector(`[data-id="${postId}"]`);
    let input = form.querySelector(".comment-input");
    let commentText = input.value.trim();

    if (commentText === "") return; // Ignore empty comments

    let id = parseInt(postId);
    let URL = `https://blog-udis.onrender.com/comment_api/${id}/`;

    // Send the comment to the server
    comment_operation(URL, commentText).then(response => {
        if (response) {
            // Find the comment section
            let commentSection = document.getElementById(`comments-${postId}`);

            // Create a new comment element
            let newComment = document.createElement("p");
            newComment.classList.add("comment");
            newComment.textContent = `${username} : ${commentText}`;

            // Append the new comment
            commentSection.appendChild(newComment);

            // Clear input field after posting
            input.value = "";
        }
    });
}

// Function to toggle the comment form
function toggle_comment(button, postId) {
    let form = document.querySelector(`[data-id="${postId}"]`);
    
    if (form) {
        form.style.display = (form.style.display === "none" || !form.style.display) ? "block" : "none";
    }
}

