import React from 'react';
import { useParams } from 'react-router-dom';

const UserPage = () => {
  let { id } = useParams();

  return (
    <div>
      <h1>User ID: {id}</h1>
    </div>
  );
};

export default UserPage;
