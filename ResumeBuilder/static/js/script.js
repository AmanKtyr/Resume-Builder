function generateResume() {
    const name = document.getElementById('fullName').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const address = document.getElementById('address').value;
    const skills = document.getElementById('skills').value;
    const experience = document.getElementById('experience').value;
    const education = document.getElementById('education').value;

    document.getElementById('previewName').innerText = name;
    document.getElementById('previewEmail').innerText = email;
    document.getElementById('previewPhone').innerText = phone;
    document.getElementById('previewAddress').innerText = address;
    document.getElementById('previewSkills').innerText = skills;
    document.getElementById('previewExperience').innerText = experience;
    document.getElementById('previewEducation').innerText = education;

    document.getElementById('resumePreview').style.display = 'block';
    document.querySelector('.download-btn').style.display = 'inline-block';
}

function downloadResume() {
    const resumeContent = document.getElementById('resumePreview').innerHTML;
    const blob = new Blob([resumeContent], { type: 'text/html' });
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = 'Resume.html';
    link.click();
}