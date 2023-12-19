import React from "react";
import { useState } from 'react';

const Post = ({deletePost, post}) => {
    const [isLiked, setLike] = useState({state: true, color: 'black'});

    return (
        <div className='post'>  
            <div>
                {post.fio}
                {post.tag.includes('#') ? ` ${post.tag}` : ` #${post.tag}`}
            </div>

            <div>
                {post.text}
            </div>
            
            <div>
               <button onClick={() => {setLike(isLiked.state ? {state: false, color: 'red'} : {state: true, color: 'black'})}} style={{color: isLiked.color}}>
                ❤
                </button>
            </div>
            <div className="post_delete">
                <button onClick={e => deletePost(post)}>Удалить</button>
            </div>
        </div>
    )
}

export default Post;
