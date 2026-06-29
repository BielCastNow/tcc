// Confirma exclusão

const botoesExcluir = document.querySelectorAll(".btn-delete");

botoesExcluir.forEach((btn) => {
  btn.addEventListener("click", function (event) {
    const confirmar = confirm("Deseja excluir este post?");

    if (!confirmar) {
      event.preventDefault();
    }
  });
});
