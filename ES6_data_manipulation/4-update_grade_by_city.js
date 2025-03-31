export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const foundGrade = newGrades.find((gradeObj) => gradeObj.studentId === student.id);
      return {
        ...student,
        grade: foundGrade ? foundGrade.grade : 'N/A',
      };
    });
}
