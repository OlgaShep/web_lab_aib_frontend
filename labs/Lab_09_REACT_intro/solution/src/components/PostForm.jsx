import React from "react";
import { useState } from 'react';

const PostForm = ({addPost}) => {
    const [postData, setData] = useState({fio: '', text: '', tag: ''})

    const addNewPost = (e) => {
        e.preventDefault();
        addPost({...postData, id: Date.now()})
        setData({fio: '', text: '', tag: ''})
      }

    return (
        <form className='addPost'>
            <input 
            value={postData.fio}
            onChange={e => setData({...postData, fio: e.target.value})}
            type='text' 
            placeholder='Название поста'
            ></input>

            <input 
            value={postData.text}
            onChange={e => setData({...postData, text: e.target.value})}
            type='text' 
            placeholder='Текст поста'
            ></input>

            <input 
            value={postData.tag}
            onChange={e => setData({...postData, tag: e.target.value})}
            type='text' 
            placeholder='Тэг'
            ></input>

            <button onClick={e => addNewPost(e)}>Создать пост</button>
      </form>
    )
}

export default PostForm;