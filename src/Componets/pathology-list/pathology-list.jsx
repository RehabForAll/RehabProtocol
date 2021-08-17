import React from 'react';
import './pathology-list-styles.css';
import { Pathology } from '../pathologies/pathology.componet'

export const PathologyList = props => (
    <div className="pathology-list">
        {props.pathologies.map(pathology =>( 
        <Pathology pathology = {pathology} 
        openModal = {props.openModal}/>
        ))}
    </div>
)