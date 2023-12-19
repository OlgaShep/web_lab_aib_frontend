import React from "react";
import { useState } from 'react';

const Counter = () => {
    const [count, setCount] = useState(0);

    return (
      <div>
        <div>
          <button className='btn' onClick={() => {setCount(count - 1);}}>-1</button>
          <button className='btn' onClick={() => {setCount(count + 1);}}>+1</button>
        </div>
        <div className='count-field'>
          <h1>{count}</h1>
        </div>
      </div>
    );
}


export default Counter;