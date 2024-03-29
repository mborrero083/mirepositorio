import React from "react";
import './TodoForm.css';
import { TodoContext } from "../TodoContext";

function TodoForm (){
    const[newTodoValue,setNewTodoValue] = React.useState('');
    const{
        addTodo,
        setOpenModal,
    } = React.useContext(TodoContext);
    const onChange = (event)=> {
        setNewTodoValue(event.target.value);
    };
    const onCancel = ()=> {
        setOpenModal(false);
    };
    const onSubmit = (event)=> {
        event.preventDefault();
        addTodo(newTodoValue);
        setOpenModal(false);
    };
    return (
        <form onSubmit={onSubmit}>
            <label>Escribe tu nuevo Todo</label>
            <textarea 
            value={newTodoValue}
            onChange={onChange}
            placeholder="cortar la cebolla"/>
            <div className="TodoForm-buttonContainer">
                <button
                type="button"
                className="TodoForm-button TodoForm-button--cancel"
                onClick={onCancel}>
                    Cancelar
                </button>
                <button type="submit"
                        className="TodoForm-button TodoForm-button--add">
                    Anadir
                </button>
            </div>
        </form>
    )
}

export {TodoForm};