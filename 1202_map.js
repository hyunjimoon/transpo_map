import React from 'react';

const CourseMap = () => {
  const textOffset = 20;
  const nodes = [
    // Blue track (Foundation)
    { id: '1', x: 850, y: 100, text: '1. intro to demand modeling', color: '#87CEEB', align: 'right' },
    { id: '2', x: 750, y: 200, text: '2. probability review', color: '#87CEEB', align: 'right' },
    { id: '3', x: 650, y: 300, text: '3. statistical inference; mle', color: '#87CEEB', align: 'right' },
    { id: '4', x: 550, y: 350, text: '4. hypothesis testing', color: '#87CEEB', align: 'right' },
    { id: '5', x: 450, y: 380, text: '5. sampling', color: '#87CEEB', align: 'right' },

    // Green track (Regression)
    { id: '6', x: 600, y: 200, text: '6. least squares regression', color: '#90EE90', align: 'right' },
    { id: '7', x: 550, y: 250, text: '7. multivariate regression', color: '#90EE90', align: 'right' },
    { id: '8', x: 500, y: 300, text: '8. goodness of fit', color: '#90EE90', align: 'right' },
    { id: '9', x: 450, y: 350, text: '9. violations of ols', color: '#90EE90', align: 'right' },
    { id: '10', x: 350, y: 380, text: '10. gen. least squares', color: '#90EE90', align: 'left' },
    { id: '11', x: 250, y: 380, text: '11. time series analysis', color: '#90EE90', align: 'left' },
    { id: '12', x: 150, y: 380, text: '12. IV, SEM', color: '#90EE90', align: 'left' },

    // Orange track (Choice)
    { id: '13', x: 150, y: 700, text: '13. Intro, Choice behavior', color: '#FFA500', align: 'left' },
    { id: '14', x: 200, y: 650, text: '14. Specification and estimation of logit models', color: '#FFA500', align: 'left' },
    { id: '18', x: 250, y: 600, text: '18. Nested logit', color: '#FFA500', align: 'left' },
    { id: '19', x: 300, y: 550, text: '19. Multivariate extreme value models', color: '#FFA500', align: 'left' },
    { id: '20', x: 350, y: 500, text: '20. Mixture models', color: '#FFA500', align: 'left' },
    { id: '21', x: 400, y: 450, text: '21. Simulation based estimations', color: '#FFA500', align: 'left' },
    { id: '22', x: 400, y: 200, text: '22. Bayesian estimation', color: '#FFA500', align: 'right' },
    { id: '23', x: 400, y: 150, text: '23. Stated preference methods', color: '#FFA500', align: 'right' },
    { id: '24', x: 400, y: 100, text: '24. Practical issues in SP design', color: '#FFA500', align: 'right' },

    // Red track (ML)
    { id: '15', x: 500, y: 600, text: '15. Aggregate forecasting', color: '#FF6B6B', align: 'right' },
    { id: '16', x: 550, y: 500, text: '16. Statistical tests of model specification', color: '#FF6B6B', align: 'right' },
    { id: '17', x: 600, y: 450, text: '17. Model estimation w/ alternative sampling', color: '#FF6B6B', align: 'right' },
    { id: '25', x: 200, y: 200, text: '25. ML for regression models', color: '#FF6B6B', align: 'left' },
    { id: '26', x: 100, y: 100, text: '26. ML w/ theoretical constraints', color: '#FF6B6B', align: 'left' }
  ];

  const cases = [
    { id: 'case0', x: 700, y: 250, text: 'case0' },
    { id: 'case1', x: 575, y: 225, text: 'case1' },
    { id: 'case2', x: 300, y: 380, text: 'case2' },
    { id: 'case3', x: 175, y: 675, text: 'case3' },
    { id: 'case4', x: 275, y: 575, text: 'case4' },
    { id: 'case5', x: 400, y: 175, text: 'case5' }
  ];

  return (
    <div className="w-full max-w-6xl mx-auto">
      <svg viewBox="0 0 1000 800" className="w-full">
        {/* Paths */}
        <path 
          d="M850 100 L 650 300 L 450 380" 
          stroke="#87CEEB" 
          strokeWidth="20" 
          fill="none"
        />
        <path 
          d="M100 380 L 450 380 L 600 200" 
          stroke="#90EE90" 
          strokeWidth="20" 
          fill="none"
        />
        <path 
          d="M150 700 L 400 450 L 400 100" 
          stroke="#FFA500" 
          strokeWidth="20" 
          fill="none"
        />
        <path 
          d="M100 100 L 400 450 L 600 450 M 400 450 L 500 600" 
          stroke="#FF6B6B" 
          strokeWidth="20" 
          fill="none"
        />

        {/* Intersection point */}
        <circle cx="400" cy="450" r="10" fill="white" stroke="black" strokeWidth="2" />

        {/* Nodes */}
        {nodes.map(node => (
          <g key={node.id}>
            <circle cx={node.x} cy={node.y} r="8" fill="black" />
            <text
              x={node.align === 'right' ? node.x + textOffset : node.x - textOffset}
              y={node.y}
              textAnchor={node.align === 'right' ? 'start' : 'end'}
              alignmentBaseline="middle"
              fill={node.color}
              className="text-sm"
            >
              {node.text}
            </text>
          </g>
        ))}

        {/* Case study indicators */}
        {cases.map(c => (
          <g key={c.id} transform={`translate(${c.x}, ${c.y})`}>
            <text x="5" y="0" className="text-xs">📊{c.text}</text>
          </g>
        ))}
      </svg>
    </div>
  );
};

export default CourseMap;