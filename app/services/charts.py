import random

import plotly.graph_objects as go


def create_radar_chart(yaml_data: dict) -> str:
    rings = yaml_data['rings']
    sectors = yaml_data['sectors']
    data_entries = yaml_data['data']

    # Create the radar chart
    fig = go.Figure()

    for sector in sectors:
        # Filter data for the current sector
        sector_data = [entry for entry in data_entries if entry['quadrant'] == sector]

        # Get the corresponding rings and names
        values = [rings.index(entry['ring']) + 1 for entry in sector_data]  # Using 1-based index for better spread
        names = [entry['name'] for entry in sector_data]

        # Base theta for the sector
        base_theta = sectors.index(sector) * (360 / len(sectors))

        # Adjust theta and radial distance to avoid overlap
        thetas = []
        adjusted_values = []
        for i in range(len(values)):
            # Add random offset to theta within the sector
            theta_offset = random.uniform(-15, 15)
            thetas.append((base_theta + theta_offset) % 360)

            # Add random radial distance within the respective ring range
            radial_min = values[i] - 0.5 if values[i] > 0 else 0
            radial_max = values[i] + 0.5 if values[i] < len(rings) else len(rings)
            adjusted_values.append(random.uniform(radial_min, radial_max))

        # Add scatter plot trace with text only on hover
        fig.add_trace(go.Scatterpolar(
            r=adjusted_values,
            theta=thetas,
            mode='markers',
            text=names,
            hoverinfo='text',
            name=sector
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, len(rings)],
                tickvals=list(range(1, len(rings) + 1)),
                ticktext=rings
            ),
            angularaxis=dict(
                tickvals=[i * (360 / len(sectors)) for i in range(len(sectors))],
                ticktext=sectors,
                direction='clockwise'
            )
        ),
        showlegend=True
    )
    return fig.to_html(full_html=False)
