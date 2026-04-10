function mostrarMensaje() {
    // Mostrar el mensaje de éxito
    const mensajeExito = document.getElementById("mensajeExito");
    mensajeExito.innerHTML = "¡Registro exitoso! Redirigiendo al login...";
    mensajeExito.style.display = "block";
    
    // Prevenir el envío del formulario de inmediato
    setTimeout(() => {
        // Envía el formulario manualmente después de 2 segundos
        document.getElementById("registroForm").submit();
        
        // Redirigir al login después de un breve retraso
        setTimeout(() => {
            window.location.href = loginUrl; // Usar la variable generada en el HTML
        }, 1000);
        
    }, 2000);

    // Retornar false para evitar el envío inmediato del formulario
    return false;
}
