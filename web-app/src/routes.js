import React from 'react';
import { Route } from 'react-router-dom';

import CFE from './CFE';

const BaseRouter = () => (
    <div>
        <Route exact path='/' component={CFE} />
    </div>
)

export default BaseRouter;