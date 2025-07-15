function checkAnswer(answer) {
  const correctAnswer = "Tableware";
  const feedback = document.getElementById('feedback');

  if (answer === correctAnswer) {
    feedback.textContent = "✅ Correct! Tableware means a set of dishes and utensils.";
    feedback.style.color = "green";
  } else {
    feedback.textContent = "❌ Incorrect. The correct answer is Tableware.";
    feedback.style.color = "red";
  }
}