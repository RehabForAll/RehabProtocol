import React from 'react'
import Modal from '../modal/modal'
import "./pathology-styles.css"

export const Pathology = props => (
    <div className="pathology-container" >
        <h1>{props.pathology.pathologyName}</h1>
        <h3>Phase: {props.pathology.Phase}</h3>
        {props.openModal && <Modal />}
    </div>
);