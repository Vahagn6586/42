/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 15:11:44 by vrafyan           #+#    #+#             */
/*   Updated: 2026/02/11 17:03:50 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *ptr, int ch, size_t count)
{
	const unsigned char	*p;
	size_t				i;

	p = (const unsigned char *)(ptr);
	i = 0;
	while (i < count)
	{
		if (*(p + i) == (unsigned char)ch)
		{
			return ((void *)(p + i));
		}
		++i;
	}
	return (0);
}
