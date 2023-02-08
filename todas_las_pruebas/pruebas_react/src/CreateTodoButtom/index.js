import React from "react";
import './CreateTodoButton.css';

function CreateTodoButton(props){
    const onClickButton = () => {
        props.setOpenModal(preState => !preState);
    }
    return(
        <button className="CreateTodoButton"
        onClick={onClickButton}
        >+
        </button>
    );
}

export { CreateTodoButton };