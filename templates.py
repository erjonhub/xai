HTML_TEMPLATE = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Question Answering System</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-5">
    <h2>Ask a Question</h2>
    <form method="post" action="/ask">
        <div class="form-group">
            <textarea class="form-control" name="question" rows="4" required placeholder="Enter your question here..."></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    {% if question %}
        <div class="mt-5">
            <h3>Question:</h3>
            <p><strong>{{ question }}</strong></p>
            <hr>
            <h3>Answer:</h3>
            <p>{{ answer_content }}</p>
            <button id="toggleButton" class="btn btn-info">Show Similar Questions</button>
            <div id="similarQuestions" style="display:none;">
                <h4>Similar Questions:</h4>
                <ul>
                    {% for s_question in similar_questions %}
                        <li>{{ s_question }}</li>
                    {% endfor %}
                </ul>
            </div>
        </div>
    {% endif %}
</div>
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.2/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('toggleButton').addEventListener('click', function() {
        var similarQuestions = document.getElementById('similarQuestions');
        if (similarQuestions.style.display === 'none') {
            similarQuestions.style.display = 'block';
            this.textContent = 'Hide Similar Questions';
        } else {
            similarQuestions.style.display = 'none';
            this.textContent = 'Show Similar Questions';
        }
    });
});
</script>
</body>
</html>


"""